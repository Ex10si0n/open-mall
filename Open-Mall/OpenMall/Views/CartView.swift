//
//  CartView.swift
//  OpenMall
//
//  Created by Ex10si0n Yan on 3/15/22.
//

import SwiftUI

struct CartView: View {
    var body: some View {
        let urlString: String = "https://isi-open-mall.surge.sh/#/cart"

            VStack {
                WebView(url: URL(string: urlString)!)
                    .cornerRadius(0)
                    .navigationBarTitleDisplayMode(.inline)
        }
    }
}

struct CartView_Previews: PreviewProvider {
    static var previews: some View {
        CartView()
    }
}
