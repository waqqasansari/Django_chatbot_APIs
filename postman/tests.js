// Check if the response has a valid format
pm.test("Response has a valid format", function () {
    // Parse the response JSON
    let responseBody = pm.response.json();
    
    pm.expect(responseBody).to.be.an('object');
    pm.expect(responseBody.chatbot_response).to.be.a('string');
});