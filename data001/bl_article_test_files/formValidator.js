/*
 * File           : $Header: //depot/main/template-kit/template-kit-publication/src/main/webapp/template/version/javascript/formValidator.js#11 $
 * Last edited by : $Author: shud $ $Date: 2008/02/28 $
 * Version        : $Revision: #11 $
 *
 * Copyright (C) 2007 Escenic AS.
 * All Rights Reserved.  No use, copying or distribution of this
 * work may be made except in accordance with a valid license
 * agreement from Escenic AS.  This notice must be included on
 * all copies, modifications and derivatives of this work.
 */


var positiveIntegerFilter = /^\d+$/;
var emailAddressFilter = /^([a-zA-Z0-9])+([\.a-zA-Z0-9_-])*@([a-zA-Z0-9])+(\.[a-zA-Z0-9_-]+)+$/;
var namevalid=/^([a-zA-Z ])+([\. a-zA-Z])+$/;
function Ltrim(val)
{
	return val.replace(/^\s+/,"");
}

function Rtrim(val)
{
	return val.replace(/\s+$/,"");
}

function trim(val)
{
	return Ltrim(Rtrim(val));
}

function isEmpty(form, fieldName) {
  var value = form[fieldName].value;
  return value == null || value == "" || value == "Type the answer here";
}

function validatePositiveInteger(form, fieldName, spanId, errorMessage) {
  return validateField(form, fieldName, spanId, positiveIntegerFilter, errorMessage)
}

function validateEmailAddress(form, fieldName, spanId, errorMessage) {
  return validateFieldEmail(form, fieldName, spanId,
      emailAddressFilter, errorMessage)
}
function validateName(form, fieldName, spanId, errorMessage) {
	  return validateField(form, fieldName, spanId,
	      namevalid, errorMessage)
	}

function validateField(form, fieldName, spanId, filter, errorMessage) {
  var field = form[fieldName];
  var value = field.value;

  if (filter.test(value)) {
    return true;
  }

  field.focus();
  var errorSpan = document.getElementById(spanId);
  errorSpan.innerHTML = errorMessage;
  errorSpan.className = "error";
  field.style.border = '2px solid red';
  return false;
}
function validateFieldEmail(form, fieldName, spanId, filter, errorMessage) {
	  var field = form[fieldName];
	  var value = field.value;

	  if (filter.test(value)) {
	    return true;
	  }

	  field.focus();
	  var errorSpan = document.getElementById(spanId);
	  errorSpan.innerHTML = errorMessage;
	  errorSpan.className = "error";
	  field.style.border = '2px solid red';
	  return false;
	}
function validatecheckbox (form, fieldName, spanId,errorMessage) {
	  var field = form[fieldName];
	  var value = field.checked;	
	  
	  if (value){return true;}
	  var errorSpan = document.getElementById(spanId);
	  errorSpan.innerHTML = errorMessage;
	  errorSpan.className = "error";
	  return false;
	  }

function validateEmptyField(form, fieldName, spanId, errorMessage) {

  var field = form[fieldName];
  var errorSpan = document.getElementById(spanId);

  if (isEmpty(form,fieldName)) {
    field.focus();
    errorSpan.innerHTML = errorMessage;
    errorSpan.className = "error";
    field.style.border = '2px solid red';
    return false;
  } else {
    return true;
  }
}
	
function validateCaptcha(form, fieldName, spanId, errorMessage) {

	  var field = form[fieldName];
	  var errorSpan = document.getElementById(spanId);
	  
	  var d = document.getElementById('numsCap').value;
        if (d != c)

	 {
	    field.focus();
	    errorSpan.innerHTML = errorMessage;
	    errorSpan.className = "error";
	    field.style.border = '2px solid red';
	    return false;
	  } 
	  else {
	    return true;
	  }
	}	
	
	
function revertToNormalField(form, fieldName, spanId) {
  var field = form[fieldName];
  var errorSpan = document.getElementById(spanId);
  if (errorSpan) {
    errorSpan.innerHTML = "";
    field.style.border = '1px solid #eeeeee';
  }
}

function checkdate(form, fieldName, spanId){
	var validformat=/^\d{2}\/\d{2}\/\d{4}$/; //Basic check for format validity
	var field = form[fieldName];
	var errorSpan = document.getElementById(spanId);
	var success=false;
	if (!validformat.test(field.value))
		alert("Invalid Date Format. Please correct and submit again.");
	else{ //Detailed check for valid date ranges
		var monthfield=field.value.split("/")[1];
		var dayfield=field.value.split("/")[0];
		var yearfield=field.value.split("/")[2];
		var dayobj = new Date(yearfield, monthfield-1, dayfield);
		if ((dayobj.getMonth()+1!=monthfield)||(dayobj.getDate()!=dayfield)||(dayobj.getFullYear()!=yearfield))
			alert("Invalid Day, Month, or Year range detected. Please correct and submit again.");
		else
			success=true;
	}
	if (success==false) field.select()
	return success ;
}


function validateCommentForm(form, nameErrorMessage, bodyErrorMessage,emailErrorMessage, captchaErrorMessage, NlpCaptchaErrorMessage) {
  
  var success = true;
    
  if (validateEmptyField(form, 'name', 'forum.comment.error', nameErrorMessage)) {
    revertToNormalField(form, 'name', 'forum.comment.error');
  } else {
    success = false;
  }
  if (validateEmptyField(form, 'email', 'errors.email.invalid', emailErrorMessage)) {
	    revertToNormalField(form, 'email', 'errors.email.invalid');
	  } else {
	    success = false;
	  }
	 
 
  if (validateEmptyField(form, 'body', 'forum.body.error', bodyErrorMessage)) {
    revertToNormalField(form, 'body', 'forum.body.error');
  } else {
    success = false;
  }
  if (validateName(form, 'name', 'forum.comment.error', nameErrorMessage)) {
	    revertToNormalField(form, 'name', 'forum.comment.error');
	  } else {
	    success = false;
	  }
  if (validateEmailAddress(form, 'email', 'errors.email.invalid', emailErrorMessage)) {
	    revertToNormalField(form, 'email', 'errors.email.invalid');
	  } else {
	    success = false;
	  }
/*
if (validateCaptcha(form, 'numsCap', 'forum.comment.captcha.error', captchaErrorMessage)) {
	    revertToNormalField(form, 'numsCap', 'forum.comment.captcha');
	  } else {
	    success = false;
	  }

	  	var d = document.getElementById('numsCap').value;
        if (d == c) {
			revertToNormalField(form, 'numsCap', 'forum.comment.captcha.error');
		}
		else {
			success = false;
		}	   */
if(validateEmptyField (form, 'nlpAnswer', 'forum.comment.NlpCaptcha.error', NlpCaptchaErrorMessage)){
revertToNormalField(form, 'nlpAnswer', 'forum.comment.NlpCaptcha.error');
}		
else{
success = false;
}
	

  return success;
}
function regform(form) {
  
  var success = true;

   var myStringArray = $.parseJSON('[{"id":"surName","error":"<br/>Kindly enter a valid name" },{"id":"email","error":"<br/>Kindly enter a valid Email address"},{"id":"dob","error":"<br/>Kindly enter a valid Date of birth"},{"id":"agree","error":"<br/>Kindly agree to the terms and conditions"}]');
  
for (var i in myStringArray) {
    if (validateEmptyField(form, myStringArray[i].id, 'profile.'+myStringArray[i].id+'.error', myStringArray[i].error)) {
    revertToNormalField(form, myStringArray[i].id, 'profile.'+myStringArray[i].id+'.error');
  } else {
    success = false;
  }
}

if (validateName(form, myStringArray[0].id, 'profile.'+myStringArray[0].id+'.error', myStringArray[0].error)) {
	    revertToNormalField(form, myStringArray[0].id, 'profile.'+myStringArray[0].id+'.error');
	  } else {
	    success = false;
	  }
 if (validateEmailAddress(form, myStringArray[1].id, 'profile.'+myStringArray[1].id+'.error', myStringArray[1].error)) {
	    revertToNormalField(form, myStringArray[1].id, 'profile.'+myStringArray[1].id+'.error');
	  } else {
	    success = false;
	  }/*
if (validatePositiveInteger(form, myStringArray[3].id, 'profile.'+myStringArray[3].id+'.error', myStringArray[3].error)) {
	    revertToNormalField(form, myStringArray[3].id, 'profile.'+myStringArray[3].id+'.error');
	  } else {
	    success = false;
	  }	  */
if (validatecheckbox(form, myStringArray[3].id, 'profile.'+myStringArray[3].id+'.error', myStringArray[3].error)) {
	    revertToNormalField(form, myStringArray[3].id, 'profile.'+myStringArray[3].id+'.error');
	  } else {
	    success = false;
	  }	
if (checkdate(form, myStringArray[2].id, 'profile.'+myStringArray[2].id+'.error', myStringArray[2].error)) {
	    revertToNormalField(form, myStringArray[2].id, 'profile.'+myStringArray[2].id+'.error');
	  } else {
	    success = false;
	  }		  
  return success;
}

function loginform(form) {
  
  var success = true;

   var myStringArray = $.parseJSON('[{"id":"userName","error":"<br/>Kindly enter your email address" },{"id":"password","error":"<br/>Kindly enter your password"}]');
  
for (var i in myStringArray) {

    if (validateEmptyField(form, myStringArray[i].id, 'profile.'+myStringArray[i].id+'.error', myStringArray[i].error)) {
    revertToNormalField(form, myStringArray[i].id, 'profile.'+myStringArray[i].id+'.error');
  } else {
    success = false;
  }
}

 if (validateEmailAddress(form, myStringArray[0].id, 'profile.'+myStringArray[0].id+'.error', myStringArray[0].error)) {
	    revertToNormalField(form, myStringArray[0].id, 'profile.'+myStringArray[0].id+'.error');
	  } else {
	    success = false;
	  }

  return success;
}

function passwordresetform(form) {
  
  var success = true;

   var myStringArray = $.parseJSON('[{"id":"userName","error":"<br/>Kindly enter your email address" }]');
  
for (var i in myStringArray) {

    if (validateEmptyField(form, myStringArray[i].id, 'profile.'+myStringArray[i].id+'.error', myStringArray[i].error)) {
    revertToNormalField(form, myStringArray[i].id, 'profile.'+myStringArray[i].id+'.error');
  } else {
    success = false;
  }
}

 if (validateEmailAddress(form, myStringArray[0].id, 'profile.'+myStringArray[0].id+'.error', myStringArray[0].error)) {
	    revertToNormalField(form, myStringArray[0].id, 'profile.'+myStringArray[0].id+'.error');
	  } else {
	    success = false;
	  }

  return success;
}
function updateform(form) {
  
  var success = true;

   var myStringArray = $.parseJSON('[{"id":"surName","error":"<br/>Kindly enter a valid name" },{"id":"dob","error":"<br/>Kindly enter a valid Date of birth"}]');
  
for (var i in myStringArray) {
    if (validateEmptyField(form, myStringArray[i].id, 'profile.'+myStringArray[i].id+'.error', myStringArray[i].error)) {
    revertToNormalField(form, myStringArray[i].id, 'profile.'+myStringArray[i].id+'.error');
  } else {
    success = false;
  }
}

if (validateName(form, myStringArray[0].id, 'profile.'+myStringArray[0].id+'.error', myStringArray[0].error)) {
	    revertToNormalField(form, myStringArray[0].id, 'profile.'+myStringArray[0].id+'.error');
	  } else {
	    success = false;
	  }/*
if (validatePositiveInteger(form, myStringArray[2].id, 'profile.'+myStringArray[2].id+'.error', myStringArray[2].error)) {
	    revertToNormalField(form, myStringArray[2].id, 'profile.'+myStringArray[2].id+'.error');
	  } else {
	    success = false;
	  }	  */
if (checkdate(form, myStringArray[1].id, 'profile.'+myStringArray[1].id+'.error', myStringArray[1].error)) {
	    revertToNormalField(form, myStringArray[1].id, 'profile.'+myStringArray[1].id+'.error');
	  } else {
	    success = false;
	  }	
  return success;
}

function changepasswordform(form) {
  
  var success = true;

   var myStringArray = $.parseJSON('[{"id":"oldPassword","error":"<br/>Kindly enter your old password" },{"id":"password","error":"<br/>Kindly enter your new password"},{"id":"confirmPassword","error":"<br/>Kindly retype your new password"}]');
  
for (var i in myStringArray) {
    if (validateEmptyField(form, myStringArray[i].id, 'profile.'+myStringArray[i].id+'.error', myStringArray[i].error)) {
    revertToNormalField(form, myStringArray[i].id, 'profile.'+myStringArray[i].id+'.error');
  } else {
    success = false;
  }
}
 return success;
}

function listServerSubscriptionForm(form) {
  
  var success = true;

   var myStringArray = $.parseJSON('[{"id":"subscriberAddress","error":"<br/>Kindly enter your email address" }]');
  
for (var i in myStringArray) {

    if (validateEmptyField(form, myStringArray[i].id, 'nl.'+myStringArray[i].id+'.error', myStringArray[i].error)) {
    revertToNormalField(form, myStringArray[i].id, 'nl.'+myStringArray[i].id+'.error');
  } else {
    success = false;
  }
}

 if (validateEmailAddress(form, myStringArray[0].id, 'nl.'+myStringArray[0].id+'.error', myStringArray[0].error)) {
	    revertToNormalField(form, myStringArray[0].id, 'nl.'+myStringArray[0].id+'.error');
	  } else {
	    success = false;
	  }

  return success;
}
