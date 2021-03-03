$(function(){

    var getUrlParameter = function getUrlParameter(sParam) {
        var sPageURL = window.location.search.substring(1),
            sURLVariables = sPageURL.split('&'),
            sParameterName,
            i;
    
        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');
    
            if (sParameterName[0] === sParam) {
                return typeof sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
            }
        }
        return false;
    };

    var productId = getUrlParameter('id')
    var nextProductId = parseInt(getUrlParameter('id')[1])+1
    
    $.ajax({
        url: "http://localhost:9808/api/product?id="+getUrlParameter('id'),
        type: 'GET',
        dataType: 'json',
        success: function(res) {

            var verifiedPurchase = function verifiedPurchase(verified){
                if(verified == 1){
                    return "Verified Purchase"
                }else{
                    return ""
                }
            }

            $("#product-container").append(`
                <img src='static/images/`+res[0].productId+`.jpg'>
                <div>
                    <p id="description">`+res[0].description+`
                    </p>
                </div>
            `)
            
            for(i=0;i<res.length;i++){
                r = res[i]
                $("#review-container").append(`
                    <div id='review-container-inner'>
                        <img src='static/images/user.jpeg'>
                        <span id="user">UserXXX</span>
                        <div id="verified">`+verifiedPurchase(r.verified)+`</div>
                        <div id="review">`+ r.text +`</div>
                        <div id="rating-container">
                            <div id="rating">
                                <input type="radio" id="1" name=`+r.reviewType+` value = "Not Helpful At All"><br>
                                <label>Not Helpful At All</label>
                            </div>
                            <div id="rating">
                                <input type="radio" id="2" name=`+r.reviewType+` value ="Not Very Helpful"><br>
                                <label>Not Very Helpful</label>
                            </div>
                            <div id="rating">
                                <input type="radio" id="3" name=`+r.reviewType+` value = "Not Sure"><br>
                                <label>Not Sure</label>
                            </div>
                            <div id="rating">
                                <input type="radio" id="4" name=`+r.reviewType+` value = "Somehow Helpful"><br>
                                <label>Somehow Helpful</label>
                            </div>
                            <div id="rating">
                                <input type="radio" id="5" name=`+r.reviewType+` value = "Very Helpful"><br>
                                <label>Very Helpful</label>
                            </div>                    
                        </div>
                    </div>
                `)
            }

        },
        error: function(err){
            console.log("err", err)
        }
    });

    $('form#review').on('submit', function(event) {
        event.preventDefault();
        
        var formData = $('form').serializeArray()
        var userId = sessionStorage.getItem("userId")
        // var userId = "u1"
        formData.push({
            name: "userId",
            value: userId
        })

        formData.push({
            name: "productId",
            value: productId
        })

        $.ajax({
            url: 'http://localhost:9808/api/product/store_rating',
            type: 'POST',
            data: $.param(formData),
            success: function(res) {
                if(res == "success"){

                    if (productId == 10){
                        window.location.href = '/thankyou'
                    }else{
                        window.location.href = '/product?id=p'+ nextProductId;
                    }
                } else {

                }
            },
            error: function(err){
                console.log("err", err)
            }
        });
    });

})