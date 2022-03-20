//
//  OrderView.swift
//  OpenMall
//
//  Created by Ex10si0n Yan on 3/15/22.
//

import SwiftUI

struct OrderView: View {
    var body: some View {
        let urlString: String = "http://isi-open-mall.surge.sh/#/order"
            VStack {
                WebView(url: URL(string: urlString)!)
                    .cornerRadius(0)
                    .navigationBarTitleDisplayMode(.inline)
        }
    }
}

struct OrderView_Previews: PreviewProvider {
    static var previews: some View {
        OrderView()
    }
}
