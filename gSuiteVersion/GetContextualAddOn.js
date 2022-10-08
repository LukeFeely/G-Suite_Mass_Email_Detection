//import 'google-apps-script';

/**
 * Returns the contextual add-on data that should be rendered for
 * the current e-mail thread. This function satisfies the requirements of
 * an 'onTriggerFunction' and is specified in the add-on's manifest.
 *
 * @param {Object} event Event containing the message ID and other context.
 * @returns {Card[]}
 */
function getContextualAddOn(event) {
  var message = getCurrentMessage(event);
  var prefill = [getEmailBody(message)];
  var result = checkEmail(message);
  
  var emailBody = message.getPlainBody();
 
  var hashValue = MD5(removeNewLines(removeWhiteSpace(removeNouns(emailBody))));
  var responseCount = checkHashPresent(hashValue);
  
  /* response object has the form
  {
  hashVal : <the value of hashValue above>,
  count : <the count returned from the API>,
  method : <whether the hashvalue was "updated"|"created"> 
  }
  */
 
  var responseObject = {
    count: responseCount,
    hashVal: hashValue,
    method: (responseCount == 1) ? "created" : "updated",
  }
  
  var card = createDetectedCard(prefill, result, responseObject);

  return [card.build()];
}


// Take in the email
function getCurrentMessage(event) {
  var accessToken = event.messageMetadata.accessToken;
  var messageId = event.messageMetadata.messageId;
  GmailApp.setCurrentMessageAccessToken(accessToken);
  return GmailApp.getMessageById(messageId);
  
}


function getEmailBody(message){
  var emailBody = message.getBody();
  return emailBody;
}

//Simple check function - gets the email sender
function checkEmail(message){
  var sender = message.getFrom();
  return sender;
}
