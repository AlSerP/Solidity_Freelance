pragma solidity >=0.6.0 <=0.6.8;

contract Income{
    address owner;
    uint16 value;
    constructor(){
        owner = msg.sender;
    }
    
    function getEther(uint16 tmp_value) public payable{
        require(msg.value>=tmp_value);
        
    }
    function transEther(address payable recipient,uint16 tmp_value) payable external{
        transfer(recipient,tmp_value wei);
    }
}