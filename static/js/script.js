// static/js/script.js
// small bits of frontend interaction

document.addEventListener('DOMContentLoaded', function () {
    // filter the task cards by priority on the dashboard
    const priorityFilter = document.getElementById('priority-filter');
    if (priorityFilter) {
        priorityFilter.addEventListener('change', function () {
            const tasks = document.querySelectorAll('.task-card');
            const selected = this.value;
            tasks.forEach(function (task) {
                if (selected === 'all' || task.dataset.priority === selected) {
                    task.style.display = 'block';
                } else {
                    task.style.display = 'none';
                }
            });
        });
    }

    // auto-dismiss flash messages if we ever show any
    const messages = document.querySelectorAll('.flash-message');
    messages.forEach(function (msg) {
        setTimeout(function () {
            msg.style.transition = 'opacity 0.5s';
            msg.style.opacity = '0';
            setTimeout(function () { msg.remove(); }, 500);
        }, 3000);
    });
});
