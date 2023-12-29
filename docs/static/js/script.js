$(document).ready(function () {
    /*
     * For sidebarToggled
    */
    const sidebarToggleBtn = $('#sidebarToggleBtn');

    if (sidebarToggleBtn.length) {
        if (localStorage.getItem('amjSidebarToggle') === 'true') {
            $('body').toggleClass('sidebarToggled');
        }

        sidebarToggleBtn.on('click', function (event) {
            event.preventDefault();
            $('body').toggleClass('sidebarToggled');

            localStorage.setItem('amjSidebarToggle', $('body').hasClass('sidebarToggled'));
        });
    }
});