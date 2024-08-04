// cypress/support/pages/loginPage.js
class loginPagePO {
    visit() {
      cy.visit('/login');
    }
  
    fillUsername(username) {
      cy.get('#username').type(username);
    }
  
    fillPassword(password) {
      cy.get('#password').type(password);
    }
  
    submit() {
      cy.get('#loginButton').click();
    }
  
    getErrorMessage() {
      return cy.get('#errorMessage');
    }
  }
  
  module.exports = new loginPagePO  