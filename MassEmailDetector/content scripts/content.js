const MASS_EMAIL_CUTOFF = 10; //if been hashed > 10 times; likely a mass email
var currentEmail;
console.log("running");
document.addEventListener('click', () => alert('click'));//test if working at all
/*
    NOTES
      -Remaking some of seans stuff,
      -Hashing & nouns & whitespace
      -Need to find way to get email body when opened ->
          listen for URL change and if matches gmail/hash parse body as string , REMOVING DIVS ETC
      -Then hash body and POST hash to update hash value
      -Then GET hash to retrieve value in database.
      -Need to find way to display a sign when hovering email -> could use alert() if too hard.
      -
*/



//function that returns body of email as a string
function String getBodyOfEmail(someInput){
  //copy seans
}

//function that removes nouns from a string
function String removeNouns(String text){
  //copy seans
  return text;
}

//function that removes whitespace from a string
function String removeWhiteSpace(String text){
  //copy seans
  return text;
}

//function that hashes email body will then use result to call below
function hashBody(String emailBody){
  String hash = "HASHMETHOD";
  //insert hash method
  return hash;
}

//post function to update hashes

function getNumberOfHashes(String api_address, String hash){
  var ourRequest = new XMLHttpRequest();
  var url = api_address + '/' + hash;
  ourRequest.open('GET',url);
  //when request loads
  ourRequest.onload = function () {
    //parse to JSON
    var numberOfHashes = JSON.parse(ourRequest.responseText);
    return numberOfHashes;
  };
}

function isEmail(String currentURL){
  //check if it is extension of standard gmail URL
  //if length > standard url.length = is email
}

//function that alerts user of mass emailBody

//function that listens for DOM Loaded && isEmail and runs above functions


//progress to injects icon
