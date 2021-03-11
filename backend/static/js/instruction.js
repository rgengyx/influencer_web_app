$(function(){

    $('form#start-experiment').on('submit', function(event) {
        event.preventDefault();


        var combo =  Math.floor(Math.random() * 400)
        $.ajax({
            url: "http://localhost:9808/api/product/get_order?combo="+combo,
            type: "GET",
            dataType: "JSON",
            success: function(res){
                sessionStorage.setItem("product_order", JSON.stringify(res));
                window.location.href = '/product?id='+res[0][0];
            }
        })
    });

})
