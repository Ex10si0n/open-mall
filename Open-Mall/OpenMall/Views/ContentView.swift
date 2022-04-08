//
//  ContentView.swift
//  OpenMall
//
//  Created by Ex10si0n Yan on 3/15/22.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            TabView() {
                ShopView().tabItem {
                    VStack {
                        Image(systemName: "bag")
                        Text("Shop")
                    }
                }.tag(1)
                ProfileView().tabItem {
                    VStack {
                        Image(systemName: "person")
                        Text("Profile")
                    }
                }.tag(2)
                CartView().tabItem {
                    VStack {
                        Image(systemName: "cart")
                        Text("Cart")
                        
                    }
                }.tag(3)
                OrderView().tabItem {
                    VStack {
                        Image(systemName: "creditcard")
                        Text("Orders")
                    }
                }.tag(4)
            }}
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
