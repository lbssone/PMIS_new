$(document).ready(function() {
    $('.ui.menu').menu();
});

$('.ui .item').tab();

$('.ui .item').on('click', function() {
    $('.ui .item').removeClass('active');
    $(this).addClass('active');
 }); 