async function loadHomeStats() {

    try {

        const token =
            localStorage.getItem(
                "access_token"
            );

        const response =
            await fetch(
                "/analytics/summary",
                {
                    headers: {
                        "Authorization":
                            `Bearer ${token}`
                    }
                }
            );

        if (!response.ok) {

            return;
        }

        const data =
            await response.json();

        document.getElementById(
            "total-predictions"
        ).innerText =
            data.total_predictions;

        document.getElementById(
            "guest-categories"
        ).innerText =
            data.total_clusters;

        document.getElementById(
            "top-cluster"
        ).innerText =
            data.top_cluster;

        document.getElementById(
            "model-type"
        ).innerText =
            "PCA + KMeans";

    } catch (error) {

        console.error(
            "Home statistics error:",
            error
        );
    }
}

loadHomeStats();
