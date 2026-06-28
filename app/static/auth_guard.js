async function checkAuthentication() {

    const token =
        localStorage.getItem(
            "access_token"
        );

    if (!token) {

        window.location.replace(
            "/login-page"
        );

        return;
    }

    try {

        const response = await fetch(
            "/me",
            {
                headers: {
                    "Authorization":
                        `Bearer ${token}`
                }
            }
        );

        if (!response.ok) {

            localStorage.removeItem(
                "access_token"
            );

            window.location.replace(
                "/login-page"
            );

            return;
        }

        const user = await response.json();

        localStorage.setItem(
            "current_user",
            JSON.stringify(user)
        );

        renderCurrentUser(user);
        renderAdminNavigation(user);
        protectAdminPage(user);

    } catch (error) {

        console.error(
            "Authentication check failed:",
            error
        );
    }
}

function renderCurrentUser(user) {

    const navbar =
        document.querySelector(
            ".top-navbar"
        );

    if (
        !navbar ||
        document.getElementById(
            "current-user-badge"
        )
    ) {

        return;
    }

    const roleLabel =
        user.role === "admin"
            ? "Admin"
            : "Hotel User";

    const badge =
        document.createElement(
            "div"
        );

    badge.id =
        "current-user-badge";

    badge.className =
        "current-user-badge";

    badge.innerHTML =
        `<span>Welcome, ${user.name}</span><strong>${roleLabel}</strong>`;

    const themeToggle =
        navbar.querySelector(
            ".theme-toggle"
        );

    navbar.insertBefore(
        badge,
        themeToggle
    );
}

function renderAdminNavigation(user) {

    if (user.role !== "admin") {

        return;
    }

    const sidebar =
        document.querySelector(
            ".sidebar"
        );

    if (
        !sidebar ||
        document.getElementById(
            "admin-nav-link"
        )
    ) {

        return;
    }

    const adminLink =
        document.createElement(
            "a"
        );

    adminLink.id =
        "admin-nav-link";

    adminLink.href =
        "/admin";

    adminLink.innerHTML =
        '<i class="fas fa-user-shield"></i> Admin';

    if (
        window.location.pathname === "/admin"
    ) {

        adminLink.classList.add(
            "active"
        );
    }

    const logoutLink =
        sidebar.querySelector(
            ".logout-link"
        );

    sidebar.insertBefore(
        adminLink,
        logoutLink
    );
}

function protectAdminPage(user) {

    if (
        window.location.pathname === "/admin"
        &&
        user.role !== "admin"
    ) {

        window.location.replace(
            "/"
        );
    }
}

document.addEventListener(
    "DOMContentLoaded",
    checkAuthentication
);

window.addEventListener(
    "pageshow",
    checkAuthentication
);
