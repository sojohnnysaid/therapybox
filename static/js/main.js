$(document).ready(function() {
    $('.js-example-basic-multiple').select2();
});


function checkAll(){
    $('#select_all').change(function () {
        var checkboxes = $(this).closest('form').find(':checkbox');
        checkboxes.prop('checked', $(this).is(':checked'));
    });
}


function addToCart(id){
    if (!'cart' in localStorage){
        cart = {'items': []}
        localStorage.cart = JSON.stringify(cart)
    }

    try {
        cart = JSON.parse(localStorage.cart)
        cart['items'].push(id)
    } catch (error) {
        cart = {'items': []}
        localStorage.cart = JSON.stringify(cart)
        cart = JSON.parse(localStorage.cart)
        cart['items'].push(id)
        localStorage.cart = JSON.stringify(cart)
        console.log(localStorage.cart)
    }
}