// static/js/script.js
// Gundam UI interactions and dashboard logic

document.addEventListener("DOMContentLoaded", () => {

    /* ============================================================
       PRIORITY FILTER — Dashboard
       ============================================================ */
    const priorityFilter = document.getElementById("priority-filter");
    if (priorityFilter) {
        priorityFilter.addEventListener("change", () => {
            const tasks = document.querySelectorAll(".task-card");
            const selected = priorityFilter.value;

            tasks.forEach(task => {
                if (selected === "all" || task.dataset.priority === selected) {
                    task.style.display = "block";
                } else {
                    task.style.display = "none";
                }
            });
        });
    }

    /* ============================================================
       GUNDAM BUTTON GLOW — Hover Pulse
       ============================================================ */
    document.querySelectorAll(".btn-primary").forEach(btn => {
        btn.addEventListener("mouseenter", () => {
            btn.style.boxShadow = "0 0 12px rgba(242, 201, 76, 0.6)";
        });
        btn.addEventListener("mouseleave", () => {
            btn.style.boxShadow = "none";
        });
    });

    /* ============================================================
       FADE-IN ANIMATION — Hologram Boot Sequence
       ============================================================ */
    document.querySelectorAll(".task-card, .task-form").forEach(el => {
        el.classList.add("fade-in");
    });

    /* ============================================================
       AUTO-DISMISS FLASH MESSAGES
       ============================================================ */
    const messages = document.querySelectorAll(".flash-message");
    messages.forEach(msg => {
        setTimeout(() => {
            msg.style.transition = "opacity 0.5s";
            msg.style.opacity = "0";

            setTimeout(() => {
                msg.remove();
            }, 500);
        }, 3000);
    });

});
