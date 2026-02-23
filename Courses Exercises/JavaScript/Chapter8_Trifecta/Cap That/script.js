const memeArray = [
  "https://i.imgur.com/bSi4xLb.png",
  "https://i.imgur.com/6y0G7N0.png",
  "https://i.imgur.com/LXnRao1.png",
  "https://i.imgur.com/Qqoxh1N.png"
];

const memeCaptions = [
  "Me calculating exactly how much sleep I'll get if I fall asleep right this second.",
  "When the coffee kicks in but it's just anxiety.",
  "My brain at 3 AM: Let's review every embarrassing thing you did in 2014.",
  "I'm not procrastinating, I'm doing side quests.",
  "Me ignoring the red flags because they match my outfit.",
  "That terrifying moment you accidentally open the front-facing camera.",
  "My bank account looking at my online shopping cart.",
  "When you finally find a comfortable sleeping position and realize you have to pee.",
  "Telling myself I'll only watch one more episode (a lie).",
  "Me pretending to work when the boss walks by.",
  "When someone texts 'we need to talk' and my soul leaves my body.",
  "My diet officially starting 'tomorrow' for the 400th day in a row.",
  "When the Wi-Fi drops by one bar and suddenly we're in the Stone Age.",
  "My reaction to my own entirely avoidable poor decisions.",
  "When someone asks what I bring to the table and I point to my sparkling personality.",
  "My patience physically leaving my body.",
  "Me looking at the completely overwhelming mess I just made.",
  "When the group chat is going off but you're pretending to be a productive member of society.",
  "My pet judging me for eating a family-sized bag of chips alone.",
  "When you try to be a responsible adult for one (1) day.",
  "Me staring out the window waiting for a package I ordered 10 minutes ago.",
  "My single remaining brain cell working overtime to process basic instructions.",
  "When you're forced to participate in a corporate icebreaker.",
  "Me re-reading the email I just sent to make sure I sound like a genius.",
  "When the 'quick 5-minute fix' takes three hours and a blood sacrifice.",
  "My wallet begging for mercy at the checkout line.",
  "When you suddenly remember tomorrow is Monday.",
  "Me trying to gracefully exit a conversation I never wanted to be in.",
  "When the password must contain a capital letter, a number, a symbol, and a drop of unicorn blood.",
  "My alarm clock looking at me with pure malice.",
  "When you say 'sounds good!' but internally you are screaming.",
  "Me trying to focus on literally anything that isn't my phone.",
  "When you spot someone you vaguely know in public and immediately perform evasive maneuvers.",
  "My immune system trying to run on 4 hours of sleep and iced coffee.",
  "When you hit your pinky toe on the furniture and see the face of God.",
  "Me aggressively scrolling to the bottom to 'read' the terms and conditions.",
  "When the GPS says 'recalculating' and you know you've messed up.",
  "My motivation hiding exactly when I need it most.",
  "When you laugh at a joke and then slowly realize it's about you.",
  "Me accepting my fate after looking at my screen time report.",
  "That moment you hit 'Reply All' by mistake and accept that you must change your identity.",
  "Me acting surprised when my actions have consequences.",
  "When the restaurant food arrives and everyone has to wait for the photo shoot.",
  "My face when I realize I have to actually socialize this weekend.",
  "Me trying to hold my life together with sheer willpower and duct tape.",
  "When you're the only one who didn't understand the joke but you laugh anyway.",
  "Me explaining my highly flawed logic to my friends.",
  "When you step on a Lego and enter a new dimension of pain.",
  "My face when someone says they don't like dogs.",
  "Me confidently giving directions when I have absolutely no sense of direction."
];

const randomMeme = document.getElementById("random-meme");
const randomCaption = document.getElementById("random-caption");
const generatorButton = document.getElementById("generator-button");

function memeGenerator(){
    let randomIndex1 = Math.floor(Math.random()*memeArray.length);
    let randomIndex2 = Math.floor(Math.random()*memeCaptions.length);

    randomMeme.src = memeArray[randomIndex1];
    randomCaption.innerText = memeCaptions[randomIndex2];

}
generatorButton.addEventListener("click", memeGenerator);