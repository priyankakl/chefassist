//saving the recipe form data as a json
$("#form-submit").on("click", function(){
    let title= $('#inputtitle').val();
    let ingredients = $('#inputingredients').val()
    let instructions = $('#inputinstructions').val();
    let notes = $('#inputnotes').val();
    let total_time = $('#total_time').val();
    console.log(notes)
    console.log(ingredients)
    console.log("test")

    let payload={
        title: title, 
        ingredients: ingredients,
        instructions:instructions,
        notes:notes,
        total_time:total_time,
    };
    $.ajax({
        url:"/api/add_recipe/",
        type: "POST",
        data: payload,
        dataType:"json",
        success:function(response){
            console.log("Sent!")
            alert("Recipe successfully added!")
            document.getElementById("inputtitle").value = ""
            document.getElementById("inputingredients").value = ""
            document.getElementById("inputinstructions").value = ""
            document.getElementById("inputnotes").value = ""
            document.getElementById("total_time").value = ""
        }
    })
});

//Displaying the recipes in the frontend in the form of cards
    $.ajax({
        url: "/api/recipes/",
        type: "GET",
        success: function(response) {  
            console.log(response)  
            for (let recipe of response) {
                console.log(recipe)
                let card = `<div class="column">
                                <div class="card" >
                                    <div class="card-header" style="background-color:white;">
                                    <h5 class="card-title">${recipe.title}</h5>
                                    </div>
                                    <div class="card-body" style="margin-left: auto;margin-right: auto;padding-left: 0px;padding-right: 0px;">
                                    <h6 class="card-title">${recipe.ingredients}</h6>
                                    <br>
                                    <p class="card-text">Duration: ${recipe.total_time} mins</p>
                                    </div>
                                    <div class="card-footer" style="background-color:white;">
                                    <a class="btn btn-primary" href="/api/update_recipe/${recipe.title}/" role="button">Edit</a>
                                    <input type="submit" value="Start" class="start btn btn-primary" data-toggle="modal" data-target="#myModal" data-time="${recipe.total_time}" data-text="${recipe.instructions}"/>
                                    </div>  
                                </div>
                            </div>`
                $("#cards").append(card)
            }
        }
    });

//Text to speech and timer logic
$(document).on('click', '.start', function(){
    console.log("I'm in");
    let mins = $(this).data('time');
    let text = $(this).data('text');
    for(x in text){
        text=text.replace(".", `<br>`+",");
    }   
    var msg = new SpeechSynthesisUtterance(text);
    var voices = window.speechSynthesis.getVoices();
    msg.default=false;
    msg.voice = voices[1];
    msg.voiceURI = 'native';
    msg.volume = 1; // 0 to 1
    msg.rate = 1; // 0.1 to 10
    msg.pitch = 0; //0 to 2
    // window.speechSynthesis.cancel();
    window.speechSynthesis.speak(msg);
    console.log(mins);
    var countDownDate = new Date();

    countDownDate.setSeconds(countDownDate.getSeconds() + (parseInt(mins)*60));
    // Find the distance between now and the count down date
    
    var x = setInterval(function() {

        console.log("Timer part");
        var now = new Date();
        // Get today's date and time
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
        // Display the result in the element with id="demo"
        let timertext = days + "d " + hours + "h "
        + minutes + "m " + seconds + "s ";        

        document.getElementById("tick").innerHTML = timertext;
        document.getElementById("tick1").innerHTML = text;

        //To stop the speech 
        $("#close").on("click", function(){
            console.log("came inside1");
            window.speechSynthesis.cancel();
            clearInterval(x);
        }); 
        
        //To pause the speech in between
        $("#pause").on("click", function(){
            console.log("came inside2");
            window.speechSynthesis.pause();
            
        });  
        
        //To resume the speech 
        $("#resume").on("click", function(){
            console.log("came inside3");
            window.speechSynthesis.resume();
            
        }); 

        // If the count down is finished, write some text
        if (distance < 0) {
          clearInterval(x);
          $(".tick").text = "EXPIRED";
        }
      }, 1000);

});

//Updating the recipe 
$("#update-form-submit").on("click", function(){
    let title= $('#inputtitle').val();
    let ingredients = $('#inputingredients').val();
    let instructions = $('#inputinstructions').val();
    let notes = $('#inputnotes').val();
    let total_time = $('#total_time').val();
    console.log(notes)
    console.log("test")

    let payload={
        title: title, 
        ingredients: ingredients,
        instructions:instructions,
        notes:notes,
        total_time:total_time,
    };
    $.ajax({
        url:"/api/update_recipe/"+ title+"/",
        type: "POST",
        data: payload,
        dataType:"json",
        success:function(response){
            console.log("Sent!")
            alert("Recipe updated successfully!")
            document.getElementById("inputtitle").value = ""
            document.getElementById("inputingredients").value = ""
            document.getElementById("inputinstructions").value = ""
            document.getElementById("inputnotes").value = ""
            document.getElementById("total_time").value = ""
        }
    })
});



    

