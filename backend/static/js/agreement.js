$(function(){

    next_disabled()

    function next_disabled(){
        $("input[name='submitbtn']").prop('disabled', true);
        $("input[name='submitbtn']").css('opacity','0.3')
    }

    function next_enabled(){
        $("input[name='submitbtn']").prop('disabled', false);
        $("input[name='submitbtn']").css('opacity','1')
    }

    $("input[name='agreement']").click(function() {
        if($("input[name='agreement']").is(':checked')) {
            console.log("agreement selected")
            next_enabled()
        }else{
            next_disabled()
        }
     });

    $('form#agreement').on('submit', function(event) {
        event.preventDefault();
        window.location.href = '/instruction';
        
        // var formData = $('form').serializeArray()
        // var userId = sessionStorage.getItem("userId")
        // formData.push({
        //     name: "id",
        //     value: userId
        // })

        // $.ajax({
        //     url: 'http://localhost:9808/api/user/store_agreement',
        //     type: 'POST',
        //     data: $.param(formData),
        //     success: function(res) {
        //         if(res == "success"){
        //             window.location.href = '/instruction';
        //         } else {

        //         }
        //     },
        //     error: function(err){
        //         console.log("err", err)
        //     }
        // });
    });

})
