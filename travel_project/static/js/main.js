// Add date validation for booking form
document.addEventListener('DOMContentLoaded', function() {
    const startDate = document.getElementById('id_start_date');
    const endDate = document.getElementById('id_end_date');

    if (startDate && endDate) {
        // Set minimum date as today
        const today = new Date().toISOString().split('T')[0];
        startDate.min = today;
        endDate.min = today;

        // Ensure end date is not before start date
        startDate.addEventListener('change', function() {
            endDate.min = startDate.value;
        });
    }

    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });
});
