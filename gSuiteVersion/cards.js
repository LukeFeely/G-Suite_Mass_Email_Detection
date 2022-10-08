// UI
/*

NOTE: UI designed  by Evan Mcroary


*/
function createDetectedCard(prefill, result, responseObject){
  
  //constants
  var MASS_EMAIL_IF_OVER_THIS_NUMBER = 4;
  var NOT_MASS_EMAIL_IF_UNDER_THIS_NUMBER = 2;
  
  var card = CardService.newCardBuilder();
  card.setHeader(CardService.newCardHeader()); 
  
  try{
   
    //variables from fn input
    var countOfResponse = responseObject.count;
    var emailSenderString= result;

    //Strings
    var massEmailLikelihoodString = generateLikelihoodString(countOfResponse,MASS_EMAIL_IF_OVER_THIS_NUMBER,NOT_MASS_EMAIL_IF_UNDER_THIS_NUMBER);
    var otherUsersSectionString = 'This email has been received by ' + countOfResponse + ' other users on our system.'; 
    var errorString = 'Mass Email Detector encountered an error.';
    
    //Card sections
    var otherUsersSection = buildCardSection("Detection Result","https://cdn3.iconfinder.com/data/icons/green-business-1/750/5-512.png",otherUsersSectionString);
    var massEmailInfoSection = buildCardSection("Mass Email Likelihood","https://icon-library.net/images/fyi-icon/fyi-icon-7.jpg",massEmailLikelihoodString);
    var senderSection = buildCardSection("Email Sender","http://ichef.bbci.co.uk/news/976/cpsprodpb/12787/production/_95455657_3312a880-230e-474c-b1d9-bb7c94f8b00e.jpg",emailSenderString);
 
    card.addSection(senderSection);
    card.addSection(otherUsersSection);
    card.addSection(massEmailInfoSection);
  
  } catch (e){ 
   var errorSection = buildCardSection("Detection Error","https://www.iconsdb.com/icons/preview/red/error-4-xxl.png",e);
   card.addSection(errorSection);
  } finally {
    return card;
  }
}

//Functiont takes in a top label,icon url and content and builds a cars section
function buildCardSection(topLabel,iconUrl,content){
  var newSection =  CardService.newCardSection();
  newSection.addWidget(CardService.newKeyValue()
                       .setTopLabel(topLabel)
                       .setIconUrl(iconUrl)
                       .setContent('<b>' + content + '</b>')
                       .setMultiline(true))
  
  return newSection;
}

//Function takes in a number, and two cut off points and returns a string that is the likelihood of the email being a mass email
function generateLikelihoodString(number,highcut,lowcut){
  var massEmailStringHighLikelihood = 'High';
  var massEmailStringLowLikelihood = 'Medium';
  var massEmailStringNoLikelihood = 'Low';
  
  if(number < lowcut){
    return massEmailStringNoLikelihood;
  }
  else if(number >= lowcut && number <= highcut){
      return massEmailStringLowLikelihood ;
    }
  else if(number > highcut){
      return massEmailStringHighLikelihood;
    }
  else{
    //error -> shouldnt be here
    return "error in generateLikeliehoodString";
  }
}

