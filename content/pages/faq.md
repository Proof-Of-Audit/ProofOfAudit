Title: FAQ
Template: faq
Date: 2017-12-22

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script>
  $(document).ready(function(){
  	  $('.faq').click(function(a,b){
      $(this).next('p').slideToggle('medium')
    })
  });
</script>
<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-T8Gy5hrqNKT+hzMclPo118YTQO6cYprQmhrYwIiQ/3axmI1hQomh7Ud2hPOy8SP1" crossorigin="anonymous">


<h3 class="faq">
	Proof of Stake
<i class="fa fa-angle-down drop-down-icon" aria-hidden="true"></i></h3>

<p style="display:none">
	Proof of Stake (PoS) is a category of consensus algorithms for public blockchains that depend on a validator's economic stake in the network. In proof of work (PoW) based public blockchains (e.g. Bitcoin and the current implementation of Ethereum), the algorithm rewards participants who solve cryptographic puzzles in order to validate transactions and create new blocks (i.e. mining). In PoS-based public blockchains (e.g. Ethereum's upcoming Casper implementation), a set of validators take turns proposing and voting on the next block, and the weight of each validator's vote depends on the size of its deposit (i.e. stake). Significant advantages of PoS include security, reduced risk of centralization, and energy efficiency. Transaction Validators receive rewards in proportion to the amount of their “stake” in the network.
</p>


<h3 class="faq">
	Difference between a Delegator and a Validator
<i class="fa fa-angle-down drop-down-icon" aria-hidden="true"></i></h3>

<p style="display:none">
	A validator has an active key involved in signing votes in the consensus protocol. A validator must also have some tokens in a security deposit. Since there will only be a limitted number of validators, other token holders can delegate to the validators, thereby contributing to the economic security of the system by putting their funds on the line if the validator misbehaves. In return, they earn a share of the transaction fees and any inflationary rewards.
</p>


<h3 class="faq">
	Can Delegators also be Validators?
<i class="fa fa-angle-down drop-down-icon" aria-hidden="true"></i></h3>

<p style="display:none">
	Delegators are never validators. If a validator wishes to delegate, they need to do so with their free and unbonded tokens.
</p>

