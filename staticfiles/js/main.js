$(document).ready(function() {
    $('.js-example-basic-multiple').select2();
});


function checkAll(){
    $('#select_all').change(function () {
        var checkboxes = $(this).closest('form').find(':checkbox');
        checkboxes.prop('checked', $(this).is(':checked'));
    });
}

