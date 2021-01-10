$(document).ready(function() {
    $('.js-example-basic-multiple').select2();
});


function checkAll(){
    $('#select_all').change(function () {
        var checkboxes = $(this).closest('form').find(':checkbox');
        checkboxes.prop('checked', $(this).is(':checked'));
    });
}




function set_cookie(key, value){
    return `${key}=${value}`
}

function get_cookie(key){
    return document.cookie.split('; ').find(row=>row.startsWith(key)).split('=')[1];
}



function billingToShipping(){

    const billing_address_line_1 = $("#id_billing_address_line_1").val()
    $("#id_shipping_address_line_1").val(billing_address_line_1)

    const billing_address_line_2 = $("#id_billing_address_line_2").val()
    $("#id_shipping_address_line_2").val(billing_address_line_2)

    const billing_suburb = $("#id_billing_suburb").val()
    $("#id_shipping_suburb").val(billing_suburb)

    const billing_city = $("#id_billing_city").val()
    $("#id_shipping_city").val(billing_city)

    const billing_postcode = $("#id_billing_postcode").val()
    $("#id_shipping_postcode").val(billing_postcode)
}