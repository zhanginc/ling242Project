# Sheldon's Words - LING242 Final Project

Initally, I intended to use a recurrent neural network but had an extreme amount of difficulty downloading the necessary programs to do so. Instead I use n-gram language model to generate sentences that sound like Sheldon.

The model is trained with nearly a 1 million words from Sheldon from all the scripts of the The Big Bang Theory. The prediction of the next word invovles using the predicted probability distribution of the next word. The words above this pre-defined cutoff will then be used. 

Within my project, I still have issues accounting for the right initalization value (some sequence of words don't quite work, even with the bi-gram model; although, I can say that the implementation isn't quite there for the bigram model). Overall, with the right intialization values we can obtain fun (and somewhat gramatically correct sentences like:

where are you going to have access to this point that he expressed interest in other people. Uh, how was your date?

you are going to the mall on clearance. Now move, move, move.

you are going to pause here while Leonard is concerned that you know why you’re confused. No, her news sounded important, but what about playing games with me. I’m going to need some tea.

you are going to wrap things up. Buffy the Vampire Slayer continued on as it used to.

the news a bobcat has been activated now that the technology that went into this glass is every pathogen that calls your mouth home, sweet home. Not to mention an extremely private matter.

(...wow, it's almost like he's in this github repo)

