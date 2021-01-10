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
        console.log('creating new cart...')
        cart = {'items': []}
        localStorage.cart = JSON.stringify(cart)
        console.log(localStorage.cart)
    }

    try {
        console.log('trying to add to cart...')

        cart = JSON.parse(localStorage.cart)

        itemFound = cart['items'].find(element => element == id)
        if (!itemFound){
            cart['items'].push(id)
            localStorage.cart = JSON.stringify(cart)
            console.log('added to cart!')
            console.log(localStorage.cart)
        } else{
            console.log('item already in cart!')
        }
    } catch (error) {
        console.log('cart json invalid, creating new cart and adding ID...')
        cart = {'items': []}
        localStorage.cart = JSON.stringify(cart)
        
        addToCart(id)
    }

}