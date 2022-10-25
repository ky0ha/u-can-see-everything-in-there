/*
 * A demo of basic DE implementation.
 * 
 */

import java.util.ArrayList;
import java.util.Random;

public class DE {

	public static final int D = 2;  //dimensionality of benchmark function

	final double F = 0.5; //scaling factor
	final double CR = 0.9; //crossover probability
	final double[] LOW = { -3, -2 }; //upper boundary
	final double[] UP = { 3, 2 }; //lower boundary
	final int PS = 30; //population size
	final double MaxFEs = 5E3; //maximal number of function evaluations

	Random rnd; //generate a random number in [0, 1]
	int FEs; //used number of function evaluations
	indi[] pop; //population	
	int bestIdx; //index of the best individual


	public DE() {
		rnd = new Random();
		pop = new indi[PS];
	}

	public static void main(String[] args) {
		DE sample = new DE();
		sample.init();
		sample.iteration();
		sample.getBest();		
		System.out.printf("Best fitness=%f \n", sample.pop[sample.bestIdx].fitness);
		for (int i = 0; i < D; i++) {
			System.out.printf("x%d=%f   ", (i+1), sample.pop[sample.bestIdx].x[i]);
			if ((i + 1) % 5 == 0)
				System.out.println();
		}
	}

	
	/*
	 * To increase the number of function evaluations
	 * @count, how many times to increase
	 */
	public void increaseFEs(int count) {
		FEs += count;
	}



	/*
	 * Copy the @src individual to the @dst individual  
	 */
	public void clone(indi dst, indi src) {		
		dst.fitness = src.fitness;
		for (int i = 0; i < D; i++) {
			dst.x[i] = src.x[i];
		}
	}
	
	
	/*
	 * Save the indices of @count individuals into array @r, which are different from @idx.
	 */
	public void rndInt(int idx, int count, int[] r) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		for (int i = 0; i < PS; i++) {
			list.add(i);
		}
		list.remove(idx);
		for (int i = 0; i < count; i++) {
			int tempidx = (int) Math.floor(rnd.nextDouble() * list.size());
			r[i] = list.get(tempidx);
			list.remove(tempidx);
		}
	}

	
	/*
	 * Initialization
	 */
	public void init() {
		FEs = 0;
		for (int i = 0; i < PS; i++) {
			pop[i] = new indi();
			for (int j = 0; j < D; j++) {
				pop[i].x[j] = LOW[j] + (UP[j]-LOW[j])*rnd.nextDouble();
			}
			pop[i].fitness = Six_hump_Camel_back.f(pop[i].x); //calculate the fitness value
		}
		increaseFEs(PS);
	}

	
	/*
	 * Iteration process of DE
	 */
	public void iteration() {
		while (FEs <= MaxFEs) {
			for (int i = 0; i < PS; i++) {
				indi trialindi = new indi(); //trial individual
				clone(trialindi, pop[i]);
				int rndD = (int) Math.floor(rnd.nextDouble()*D);
				int[] r = new int[3];
				rndInt(i, 3, r);
				for (int j = 0; j < D; j++) {					
					if (rnd.nextDouble()<=CR || rndD==j) {
						trialindi.x[j] = pop[r[0]].x[j] + F*(pop[r[1]].x[j]-pop[r[2]].x[j]); // rand/1/bin
						if (trialindi.x[j]<LOW[j] || UP[j]<trialindi.x[j]) 
							trialindi.x[j] = LOW[j] + rnd.nextDouble() * (UP[j] - LOW[j]);
					}
				} //end for D
				trialindi.fitness = Six_hump_Camel_back.f(trialindi.x);
				if (trialindi.fitness < pop[i].fitness)
					clone(pop[i], trialindi);
			} //end for PS
			increaseFEs(PS);
		} //end while
	}

	
	/*
	 * Get the index of the best individual
	 */
	public void getBest() {
		bestIdx = 0;
		for (int i = 1; i < PS; i++) {
			if (pop[i].fitness < pop[bestIdx].fitness)
				bestIdx = i;
		}
	}

}
