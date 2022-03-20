//
//  ShopView.swift
//  OpenMall
//
//  Created by Ex10si0n Yan on 3/15/22.
//

import SwiftUI

struct ShopView: View {
    var body: some View {
        let urlString: String = "http://isi-open-mall.surge.sh/#/"
        VStack {
//                Text("Open Mall").font(.headline)
//                Text("Email").font(.subheadline)
            WebView(url: URL(string: urlString)!)
                .cornerRadius(0)
                .navigationBarTitleDisplayMode(.inline)
        }
    }
}


struct ShopView_Previews: PreviewProvider {
    static var previews: some View {
        ShopView()
    }
}
