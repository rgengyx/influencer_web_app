$(function(){

    $("input[name='submitbtn']").prop('disabled', true);
    $("input[name='submitbtn']").css('opacity','0.3')

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
    var product_order = JSON.parse(sessionStorage.getItem("product_order"))
    var nextProductId = null
    var review_order = null


    for(var i =0; i<product_order.length; i++){
        if (product_order[i][0] == productId){
            review_order = product_order[i][1]
        }
    }

    console.log(review_order)

    $.ajax({
        url: "http://localhost:9808/api/product?id="+getUrlParameter('id'),
        type: 'GET',
        dataType: 'json',
        success: function(res) {
            console.log("res", res)

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

            new_res = []
            
            for(j=0;j<review_order.length;j++){
                for(i=0;i<res.length;i++){  
                    if(res[i].reviewType == review_order[j]){
                        new_res.push(res[i])
                        break;
                    }
                }
            }
            
            console.log("new_res", new_res)
            
            for(i=0;i<new_res.length;i++){
                r = new_res[i]
                $("#review-container").append(`
                    <div id='review-container-inner'>
                        <img src='static/images/user.jpeg'>
                        <span id="user">UserXXX</span>
                        <div id="verified">`+verifiedPurchase(r.verified)+`</div>
                        <div id="review">`+ r.text +`</div>
                        <div id="rating-container">
                            <div id="question">Rate helpfulness</div>
                            <div id='rating-box'>
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
                    </div>
                `)
            }

            var r1 = false
            var r2 = false
            var r3 = false
            var r4 = false
            var r5 = false
            var r6 = false

            // Check if all inputs are filled
            $('input[name="r1"]').click(function(){
                console.log("r1")
                r1 = true

                isAllChecked()
            })

            $('input[name="r2"]').click(function(){
                console.log("r2")
                r2 = true

                isAllChecked()
            })

            $('input[name="r3"]').click(function(){
                console.log("r3")
                r3 = true

                isAllChecked()
            })

            $('input[name="r4"]').click(function(){
                console.log("r4")
                r4 = true

                isAllChecked()
            })

            $('input[name="r5"]').click(function(){
                console.log("r5")
                r5 = true

                isAllChecked()
            })

            $('input[name="r6"]').click(function(){
                console.log("r6")
                r6 = true

                isAllChecked()
            })

            function isAllChecked(){
                if(r1 && r2 && r3 && r4 && r5 && r6){
                    console.log("All Checked")
                    $("input[name='submitbtn']").prop('disabled', false);
                    $("input[name='submitbtn']").css('opacity','1')
                }
            }

        },
        error: function(err){
            console.log("err", err)
        }
    });


    // console.log(JSON.parse(sessionStorage.getItem("product_order")))

    $('form#review').on('submit', function(event) {
        event.preventDefault();
    
        for(var i =0; i<product_order.length; i++){
            if (product_order[i][0] == productId){
    
                if (i == product_order.length - 1){
                    window.location.href = '/thankyou'
                }
                nextProductId = product_order[i+1][0]
            }
        }

        console.log(nextProductId)

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
                window.location.href = '/product?id='+ nextProductId;
                // if(res == "success"){
                //     window.location.href = '/product?id='+ nextProductId;
                // } else {

                // }
            },
            error: function(err){
                console.log("err", err)
            }
        });
    });

})