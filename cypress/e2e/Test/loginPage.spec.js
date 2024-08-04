import loginPagePO from "../Pageobject/loginPage";

describe('Login Functionality', () => {
  const loginPage = new loginPage();

  beforeEach(() => {
    loginPage.visit();
  });

  it('should login successfully with valid credentials', () => {
    loginPage.fillUsername('validUser');
    loginPage.fillPassword('validPassword');
    loginPage.submit();
    cy.url().should('eq', 'https://yourapp.com/dashboard');
  });

  it('should fail login with invalid credentials', () => {
    loginPage.fillUsername('invalidUser');
    loginPage.fillPassword('invalidPassword');
    loginPage.submit();
    loginPage.getErrorMessage().should('be.visible');
  });

  it('should display error message when login fails', () => {
    loginPage.fillUsername('invalidUser');
    loginPage.fillPassword('invalidPassword');
    loginPage.submit();
    loginPage.getErrorMessage().should('contain', 'Invalid username or password');
  });
});
