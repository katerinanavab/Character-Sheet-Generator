document.addEventListener('DOMContentLoaded', function () {
    const dropdownButton = document.getElementById('ddButton');
    const dropdownContent = document.getElementById('ddContent');
    const tooltip = document.getElementById('ddHoverInfo');

    // Toggle dropdown display when the button is clicked
    dropdownButton.addEventListener('click', function (event) {
        dropdownContent.style.display = (dropdownContent.style.display === 'block') ? 'none' : 'block';
        event.stopPropagation();
    });

    // Hide dropdown when clicking outside
    document.addEventListener('click', function () {
        dropdownContent.style.display = 'none';
    });

    // Attach hover events to each dropdown option
    const options = dropdownContent.querySelectorAll('div');
    options.forEach(function (option) {
        option.addEventListener('mouseover', function (e) {
            // Retrieve heading and description for the tooltip
            const description = option.getAttribute('data-description');
            tooltip.innerHTML = `<p>${description}</p>`;
            tooltip.style.display = 'block';

            // Position the tooltip to the right of the hovered option
            const rect = option.getBoundingClientRect();
            let tooltipLeft = rect.right + window.scrollX + 10;
            let tooltipTop = rect.top + window.scrollY;

            // Ensure the tooltip is within the viewport
            const tooltipRect = tooltip.getBoundingClientRect();
            if (tooltipLeft + tooltipRect.width > window.innerWidth) {
                tooltipLeft = window.innerWidth - tooltipRect.width - 10;
            }
            if (tooltipTop + tooltipRect.height > window.innerHeight) {
                tooltipTop = window.innerHeight - tooltipRect.height - 10;
            }

            tooltip.style.left = `${tooltipLeft}px`;
            tooltip.style.top = `${tooltipTop}px`;

            // Debugging logs
            console.log('Tooltip content:', description);
            console.log('Tooltip position:', tooltip.style.left, tooltip.style.top);
            console.log('Tooltip display:', tooltip.style.display);
        });

        option.addEventListener('mouseout', function () {
            tooltip.style.display = 'none';
            console.log('Tooltip hidden');
        });

        // On option click, update the dropdown button text and hidden input
        option.addEventListener('click', function () {
            dropdownButton.innerText = option.innerText;
            document.getElementById('selected_species').value = option.getAttribute('data-value');
            dropdownContent.style.display = 'none';
        });
    });
});