let clusterChart = null;

async function loadAnalytics() {

    loadSummary();

    loadClusterDistribution();
}

async function loadSummary() {

    const response = await fetch(
        "/analytics/summary"
    );

    const data = await response.json();

    document.getElementById(
        "total-predictions"
    ).innerText =
        data.total_predictions;

    document.getElementById(
        "avg-confidence"
    ).innerText =
        data.average_confidence + "%";
}

async function loadClusterDistribution() {

    const response = await fetch(
        "/analytics/cluster-distribution"
    );

    const data = await response.json();

    const labels = data.map(
        item => item.cluster_name
    );

    const values = data.map(
        item => item.count
    );

    const ctx =
        document.getElementById(
            "clusterChart"
        );

    if (clusterChart) {

        clusterChart.destroy();
    }

    clusterChart = new Chart(ctx, {

        type: "pie",

        data: {

            labels: labels,

            datasets: [{

                data: values
            }]
        },

        options: {

            responsive: true,

            maintainAspectRatio: false
        }
    });
}

loadAnalytics();

setInterval(
    loadAnalytics,
    10000
);