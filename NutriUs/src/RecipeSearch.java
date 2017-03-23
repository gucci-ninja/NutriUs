public class RecipeSearch {

	public boolean isSuperSet(String[] UIngredients, String[] RIngredients) {
		if (UIngredients.length < RIngredients.length) return false;
		for(String RIng : RIngredients)
			if (!contains(UIngredients,RIng))
				return false;
		return true;
	}
	
	public boolean contains(String[] Set, String StrEle) {
		for (String S : Set)
			if (StrEle == S)
				return true;
		return false;
	}
}
