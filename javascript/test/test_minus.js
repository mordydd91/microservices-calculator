let minus = require("../minus.js")
let cmd = require("../runCmdCommand.js")
let assert = require('chai').assert;

describe('minus functionality test', () => {
 it('should return 1',   () => {assert.equal(minus.minus(3, 2) , 1)});
 it('should return -4',  () => {assert.equal(minus.minus(3, 7) , -4)});
 it('should return 5.5', () => {assert.equal(minus.minus(1.5, -4) , 5.5)});
 it('should return 0',   () => {assert.equal(minus.minus(0, 0) , 0)});
});

describe('minus as a service test', () => {
 it("should return -1", async () => {
   let result = await cmd.execute_microservice(1, 2, "minus.js")
   assert.equal(parseFloat(result) , -1)
 });
 it("should return 2", async () => {
   let result = await cmd.execute_microservice(5, 3, "minus.js")
   assert.equal(parseFloat(result) , 2)
 });
 it("should return 'NaN'", async () => {
   let result = await cmd.execute_microservice("rrr", "ff", "minus.js")
   assert.include(result, "NaN")
 });
 it("should return 'not enough args'", async () => {
   let result = await cmd.execute_microservice("", 2, "minus.js")
   assert.include(result , "not enough args")
 });
});
