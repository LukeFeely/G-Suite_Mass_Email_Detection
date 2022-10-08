//document.addEventListener('click', () => alert('click'));

//var console = chrome.extension.getBackgroundPage().console;

var app = {


};

//startup
document.addEventListener("DOMContentLoaded",function(){

});

var form = document.querySelector(".formToSend");

var submit_btn = document.getElementById("submit");
submit_btn.addEventListener("click",function(){
  var sender = document.getElementById("emailSender");
  var ebody = document.getElementById("emailBody");

  chrome.runtime.sendMessage({fn: "setSender", sender:sender.value}, function(response){
      console.log("sender sending to background");
  });
  chrome.runtime.sendMessage({fn: "setBody", sender:ebody.value}, function(response){
      console.log("body sending to background");
  });

  //make a call to the mainF function to process email body and add to database
  chrome.runtime.sendMessage(
    {
      fn: "mainF",
      sender: ebody.value
    },




    function(response){

      alert("number of people who have received mail:" + response.sendResponse);
    }
  );


});
