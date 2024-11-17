// Pattern array for alternating "BIG" or "SMALL" results
const pattern = ["big", "big", "big", "small", "big", "small", "small", "big", "small", "big"];
const periodHistory = [];
let remainingSeconds;
let currentPeriodData = {}; // Stores the current period data before updating to a new period

// Function to format the time as "MM : SS"
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSecs = seconds % 60;
    return `${String(minutes).padStart(2, ' ')}  :  ${String(remainingSecs).padStart(2, '0')}`;
}

// Function to set initial countdown based on the current system second
function setInitialCountdown() {
    const now = new Date();
    const currentSecond = now.getSeconds();
    remainingSeconds = 60 - currentSecond; // Calculate time remaining in the current minute
    document.getElementById("timer").textContent = formatTime(remainingSeconds);
}

// Function to update the period and add the result to history
function updatePeriod() {
    const now = new Date();
    const totalMinutes = now.getHours() * 60 + now.getMinutes();
    const newPattern = pattern[totalMinutes % pattern.length];

    // Generate a unique period code based on current time
    const period1m = `${now.getUTCFullYear()}${String(now.getUTCMonth() + 1).padStart(2, '0')}${String(now.getUTCDate()).padStart(2, '0')}1000${String(10001 + totalMinutes)}`;

    // Add the current period data to history before setting the new one
    if (currentPeriodData.period) {
        periodHistory.unshift(currentPeriodData);
        if (periodHistory.length > 10) periodHistory.pop(); // Keep only the last 10 entries

        // Update the history display
        const historyList = document.getElementById("period-history");
        historyList.innerHTML = periodHistory.map((item) => {
            return `<div class="history-item">
                        <span>${item.period}</span> <span class="label">(${item.pattern.toUpperCase()})</span>
                    </div>`;
        }).join('');
    }

    // Update the current period data
    currentPeriodData = { period: period1m, pattern: newPattern };
    document.getElementById("current-period").textContent = period1m;
    document.getElementById("current-label").textContent = newPattern.toUpperCase();
}

// Function to update the countdown timer every second
function updateTimer() {
    document.getElementById("timer").textContent = formatTime(remainingSeconds);
    remainingSeconds--;

    // When countdown reaches 0, reset it and update the period
    if (remainingSeconds < 0) {
        remainingSeconds = 59;
        updatePeriod(); // Adds the current period to history before resetting to a new one
    }
}

// Event listener for the "Clear History" button
document.getElementById("clear-history").addEventListener("click", () => {
    periodHistory.length = 0;
    document.getElementById("period-history").innerHTML = '';
});

// Initialize countdown based on current second and update every second
setInitialCountdown();
setInterval(updateTimer, 1000);
updatePeriod();