#This silly program generates 10 not very sensible sentences about some of our favorite cognitive scientists.
#There are word tokens as terminals, "parts of speech"/thematic roles as non terminals
#and combinatory rules for phrases and sentences.
#The final sentence involves embedding.

import random

#Here are some thematic roles / parts of speech
actor = ['Turing', 'Fodor', 'Chomsky', 'Skinner', 'Titchener']
intrans_action = ['acknolwedges', 'is shocked', 'is jealous', 'knows', 'is baffled']
trans_action = ['decimates', 'attacks', 'convinces', 'stuns', 'proselytizes']
recipient = ['the behaviorists', 'the functionalists', 'the introspectionists', 'the nucleators']
adjective = ['formidable', 'opaque', 'revolutionary', 'lauded','polemical']
instrument = ['modularity.', 'syntactic structures.', 'phenomenology.', 'methodology.', 'algorithms.']
complementizer = 'that' #closed class items
preposition = 'with his' #closed class items


for i in range(10): #generates 10 sentences
	NP1= random.choice(actor) #chooses a noun phrase for a thinker 
	NP2= random.choice(actor) #chooses a noun phrase for a thinker again
	NP3 = random.choice(recipient) #chooses a noun phrase for an audience / recipient
	NP4= random.choice(instrument) #chooses a noun phrase for the instrumement (through which the recipient will be impacted)
	NP5= random.choice(adjective) + " " + NP4 #modifies that instrument with an adjective for effect!
	V1= random.choice(intrans_action) #chooses an intransitive verb (that will follow the first thinker)
	V2= random.choice(trans_action) #chooses a transitive verb (whose action will affect the recipient)


	#Assembling phrases from the "lower level" of the syntactic tree upwards
	PP = preposition + " " + NP5 #gives you the prepositional phrase (e.g., "with his methodology")
	VP2 = V2 + " " + NP3 + " " + PP #gives you the embedded verb phrase (e.g., "stuns the behaviorists with his syntactic structures")
	S1 = NP2 + " " + VP2 #the embedded sentence, adds a noun to the verb phrase above
	CP = complementizer + " " + S1 #complementary clause: "that" + the embedded sentence 
	VP1= V1 + " " + CP #verb phrase + the complementary clause (e.g., "is shocked that...")
	embedded_sentence = NP1 + " " + VP1 #final sentence 
	print embedded_sentence