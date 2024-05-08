document.addEventListener('DOMContentLoaded', function() {
    const cells = document.querySelectorAll('.cell');
    cells.forEach(cell => {
        cell.addEventListener('click', function() {
            this.textContent = this.textContent === "X" ? "" : "X";
        });
    });

    const form = document.getElementById('testForm');
    form.addEventListener('submit', function(event) {
        const data = Array.from(document.querySelectorAll('.row')).map(row =>
            Array.from(row.querySelectorAll('.cell')).map(cell => cell.textContent)
        );
        document.getElementById('formData').value = JSON.stringify(data);
    });
});
