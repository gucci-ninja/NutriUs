package com.example.model;

import java.util.*;

public class BeerExpert {
	

	public List getBrands(String colour) {
		List brands = new ArrayList();
		if(colour.equals("amber")) {
			brands.add("Jack Amber");
			brands.add("Red Moose");
		}
		else {
			brands.add("jail ale pale");
			brands.add("Gout stout");
		}
		return brands;
	}
	
	/*public static void main(String[] args) {
		String colour = "amber";
		List<String> brand = new BeerExpert().getBrands(colour);
		System.out.println(brand.get(0));
	}*/
}
