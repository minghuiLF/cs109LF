from util import *

N_SAMPLES = 100000

# Program: Joint Sample
# ---------------------
# we can answer any probability question
# with multivariate samples from the joint,
# where conditioned variables match
def main():
	# our query is flu=1
	obs = getObservation()  #condition
	samples = sampleATon()
	prob = probFluGivenObs(samples, obs)
	print ('Observation = ', obs)
	print ('Pr(Flu | Obs) = ', prob)

# Method: Get Observation
# ---------------------
# specify the random variables that we are
# conditioning on...
def getObservation():
	fevObs = None
	fluObs = None
	undObs = 0
	tirObs = 1
	return [fluObs, undObs, fevObs, tirObs]

# Method: Probability of Flu Given Observation
# --------------------------
# Calculate the probability of flu given many
# samples from the joint distribution and a set
# of ovservations to condition on.
def probFluGivenObs(samples, obs):
	# reject all samples which don't align
	# with condition
	keepSamples = []
	for sample in samples:
		if checkObsMatch(sample, obs):
			keepSamples.append(sample)

	# from remaining, simply count...
	fluCount = 0
	for sample in keepSamples:
		[flu, und, fev, tir] = sample
		if flu == 1:
			fluCount += 1

	# counting can be so sweet...
	return float(fluCount) / len(keepSamples)

# Method: Check Observation Match
# -------------------------------
# returns true if and only if the random vars in
# the sample matches with the observed random vars
# for example:
# sample = [1, 0, 1, 1]
# obs = [None, 0, None, None]
# checkObsMatch(sample, obs) will return True
# since the only observed var (the second one) matches
def checkObsMatch(sample, obs):
	# this two lines are just for reference!
	[fluObs, undObs, fevObs, tirObs] = obs
	[fluSam, undSam, fevSam, tirSam] = sample

	# loop over all random variables
	for i in range(len(obs)):
		varObs = obs[i]
		varSam = sample[i]
		# if this random is observed, make sure it matches
		if varObs != None and varObs != varSam:
			return False
	return True

# Method: Sample A Ton
# --------------------
# chose N_SAMPLES with likelhood proportional
# to the joint distribution
def sampleATon():
	samples = []
	for i in range(N_SAMPLES):
		sample = makeSample()
		print (sample)
		samples.append(sample)
	return samples

# Method: Make Sample
# -------------------
# chose a single sample from the joint distribution
# based on the medical "Probabilistic Graphical Model"
def makeSample():
	# prior on causal factors
	flu = bern(0.1)
	und = bern(0.8)

	# choose fever based on flue
	if flu == 1: fev = bern(0.9)
	else:        fev = bern(0.05)

	# choose tired based on (undergrade and flu)
	if und == 1 and flu == 1:   tir = bern(1.0)
	elif und == 1 and flu == 0: tir = bern(0.8)
	elif und == 0 and flu == 1: tir = bern(0.9)
	else:                       tir = bern(0.1)

	# a sample from the joint has an
	# assignment to *all* random variables
	return [flu, und, fev, tir]

if __name__ == '__main__':
	main()
