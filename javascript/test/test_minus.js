let minus = require("../minus.js")
let assert = require('assert');

describe('minus functionality test', () => {
 it('should return 1', function () {assert.equal(minus.minus(3, 2) , 1)});
 it('should return -4', () => {assert.equal(minus.minus(3, 7) , -4)});
 it('should return 5.5', () => {assert.equal(minus.minus(1.5, -4) , 5.5)});
 it('should return 0', () => {assert.equal(minus.minus(0, 0) , 0)});
});

describe('minus as a service test', () => {
 it("should return -1", () => {assert.equal(parseFloat(cmd.execute_microservice(1, 2, "minus.js")) , 1)});
 it("should return 2", () => {assert.equal(parseFloat(cmd.execute_microservice(5, 3, "minus.js")) , -4)});
 it("should return 'NaN'", () => {assert.in(cmd.execute_microservice("rrr", "ff", "minus.js") , 5.5)});
 it("should return 'not enough args'", () => {assert.in(cmd.execute_microservice("", 2, "minus.js") , 0)});
});
