function toggleTheme() {

    const body =
        document.body;

    body.classList.toggle(
        "dark-mode"
    );

    const isDark =

        body.classList.contains(
            "dark-mode"
        );

    localStorage.setItem(

        "theme",

        isDark
            ? "dark"
            : "light"
    );

    updateThemeIcon();
}

function updateThemeIcon() {

    const icon =
        document.getElementById(
            "theme-icon"
        );

    if (!icon) return;

    if (

        document.body.classList.contains(
            "dark-mode"
        )

    ) {

        icon.className =
            "fas fa-sun";

    }

    else {

        icon.className =
            "fas fa-moon";
    }
}

window.addEventListener(

    "DOMContentLoaded",

    () => {

        const savedTheme =

            localStorage.getItem(
                "theme"
            );

        if (

            savedTheme ===
            "dark"

        ) {

            document.body
                .classList.add(
                    "dark-mode"
                );
        }

        updateThemeIcon();
    }
);