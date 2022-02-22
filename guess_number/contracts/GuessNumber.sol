// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract GuessNum{
    uint secretNumber;
    enum State {ACTIVE,COMPLETE}
    State public currState;
    uint balance;
    address public owner;
    // address payable OwnerBalance;

    constructor(uint _secretNumber) payable{
        require(msg.value>=10*10**18,"This contract needs to be fund with 10ETH");
        secretNumber = _secretNumber;
        balance = msg.value;
        owner = msg.sender;
    }
    function getBalance() public view returns(uint){
        return balance;
    }

    function play(address payable player,uint _numberGauess) external payable returns(uint){
        require(msg.value >= 10**18,"Pay at least one ETH to gain");
        require(currState == State.ACTIVE,"Too late");
        if(_numberGauess == secretNumber){
            player.transfer(address(this).balance);
            currState = State.COMPLETE;
            return balance;
        }else{
            owner.call{value: msg.value}("");
            return balance;
        }
    }
    modifier onlyOwner(){
        require(msg.sender == owner,"Unauthenticated");
        _;
    }
    function OwnerBalance() public onlyOwner view returns(uint256){
        return owner.balance;
    }

}