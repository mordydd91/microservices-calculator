let plus = require("../plus.js")
let cmd = require("../runCmdCommand.js")
let assert = require('chai').assert;

describe('plus functionality test', () => {
 it('plus(1,2)=3',    () => {assert.equal(plus.plus(1, 2) , 3)});
 it('plus(0,0)=0',    () => {assert.equal(plus.plus(0, 0) , 0)});
 it('plus(-1,-1)=-2', () => {assert.equal(plus.plus(-1, -1) , -2)});
});

describe('plus as a service test', () => {
 it("should return 3", async () => {
   let result = await cmd.execute_microservice(1, 2, "plus.js")
   assert.equal(parseFloat(result) , 3)
 });
 it("should return 1", async () => {
   let result = await cmd.execute_microservice(0, 1, "plus.js")
   assert.equal(parseFloat(result) , 1)
 });
 it("should return 'not enough args'", async () => {
   let result = await cmd.execute_microservice("", "1", "plus.js")
   assert.include(result, "not enough args")
 });
 it("should return 'NaN'", async () => {
   let result = await cmd.execute_microservice("da", "1", "plus.js")
   assert.include(result , "NaN")
 });
});
