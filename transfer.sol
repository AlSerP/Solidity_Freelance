pragma solidity >=0.6.0 <=0.6.8;
contract Transfer_to_user{
    function send(address payable recipient) external payable{
        recipient.transfer(msg.value);
    }
}