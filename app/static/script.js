async function predictCluster() {

    const requestBody = {

        restaurant_visits:
            parseFloat(
                document.getElementById(
                    "restaurant_visits"
                ).value
            ) || 0,

        restaurant_spend_usd:
            parseFloat(
                document.getElementById(
                    "restaurant_spend_usd"
                ).value
            ) || 0,

        room_service_orders: 0,
        room_service_spend_usd: 0,

        bar_lounge_visits: 0,
        minibar_charges_usd: 0,

        spa_treatments_count:
            parseFloat(
                document.getElementById(
                    "spa_treatments_count"
                ).value
            ) || 0,

        spa_spend_usd:
            parseFloat(
                document.getElementById(
                    "spa_spend_usd"
                ).value
            ) || 0,

        gym_checkins_count:
            parseFloat(
                document.getElementById(
                    "gym_checkins_count"
                ).value
            ) || 0,

        pool_beach_visits_count: 0,

        activity_bookings_count:
            parseFloat(
                document.getElementById(
                    "activity_bookings_count"
                ).value
            ) || 0,

        activity_spend_usd: 0,

        kids_club_sessions:
            parseFloat(
                document.getElementById(
                    "kids_club_sessions"
                ).value
            ) || 0,

        tour_bookings_count: 0,

        concierge_requests_count:
            parseFloat(
                document.getElementById(
                    "concierge_requests_count"
                ).value
            ) || 0,

        transport_requests_count:
            parseFloat(
                document.getElementById(
                    "transport_requests_count"
                ).value
            ) || 0,

        laundry_requests_count:
            parseFloat(
                document.getElementById(
                    "laundry_requests_count"
                ).value
            ) || 0,

        special_requests_count: 0,

        in_room_entertainment_hours: 0,

        gift_shop_spend_usd: 0,

        business_center_hours: 0,

        extra_housekeeping_requests: 0,

        avg_service_response_minutes: 0,

        maintenance_calls_count: 0,

        checkin_wait_minutes: 0,

        service_complaint_count: 0
    };

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict-cluster",
            {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify(
                    requestBody
                )
            }
        );

        const data = await response.json();

        displayResult(data);

    } catch (error) {

        console.error(error);

        alert(
            "Error connecting to backend."
        );
    }
}

function displayResult(data) {

    const resultContainer =
        document.getElementById(
            "result-container"
        );

    resultContainer.innerHTML = `

        <h2>
            Prediction Result
        </h2>

        <p>
            <strong>Predicted Cluster:</strong>
            ${data.predicted_cluster}
        </p>

        <p>
            <strong>Cluster Name:</strong>
            ${data.cluster_name}
        </p>

        <h3>
            Recommendations
        </h3>

        <ul>
            ${data.recommendations
                .map(
                    recommendation =>
                    `<li>${recommendation}</li>`
                )
                .join("")}
        </ul>

        <h3>
            Operational Insights
        </h3>

        <ul>
            ${data.operational_insights
                .map(
                    insight =>
                    `<li>${insight}</li>`
                )
                .join("")}
        </ul>
    `;
}