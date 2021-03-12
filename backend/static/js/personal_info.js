$(function(){

    $('#age').append("<option disabled selected value> -- </option>")
    for (i=1;i<=100;i++){
        $("#age").append($('<option></option>').val(i).html(i))
    }

    $("input[name='submitbtn']").prop('disabled', true);
    $("input[name='submitbtn']").css('opacity','0.3')

    var ageSelected = false
    var genderChecked = false
    var use_amazonChecked = false
    var read_reviewChecked = false

    // Check if all inputs are filled
    $('#age option').click(function(){
        console.log("age selected")
        ageSelected = true

        isAllChecked()
    })

    $("input[id='gender']").click(function() {
        if($("input[id='gender']").is(':checked')) {
            console.log("gender selected")
            genderChecked = true

            isAllChecked()
        }
     });

    $("input[id='use_amazon']").click(function() {
        if($("input[id='use_amazon']").is(':checked')) {
            console.log("use_amazon selected")
            use_amazonChecked = true

            isAllChecked()
        }
    });

    $("input[id='read_review']").click(function() {
        if($("input[id='read_review']").is(':checked')) {
            console.log("read_review selected")
            read_reviewChecked = true

            isAllChecked()
        }
    });


    function isAllChecked(){
        if(ageSelected && genderChecked && use_amazonChecked && read_reviewChecked){
            console.log("All Checked")
            $("input[name='submitbtn']").prop('disabled', false);
            $("input[name='submitbtn']").css('opacity','1')
        }
    }

    $('form').on('submit', function(event) {
        event.preventDefault();
        
        var formData = $('form').serializeArray()
        age = $("#age option:selected").text()
        formData.push({
            name: "age", 
            value: age
        })

        var userId = uuidv4()
        formData.push({
            name: "id",
            value: userId
        })

        $.ajax({
            url: 'http://localhost:9808/api/user/store',
            type: 'POST',
            data: $.param(formData),
            success: function(res) {
                if(res == "success"){
                    // Store
                    sessionStorage.setItem("userId", userId);
                    window.location.href = '/description';
                } else {

                }
            },
            error: function(err){
                console.log("err", err)
            }
        });
    });

    function uuidv4() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
          var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
          return v.toString(16);
        });
      }
})
