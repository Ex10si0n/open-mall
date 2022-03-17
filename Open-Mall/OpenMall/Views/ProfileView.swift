//
//  ProfileView.swift
//  OpenMall
//
//  Created by Ex10si0n Yan on 3/15/22.
//

import SwiftUI

struct ProfileView: View {
    var body: some View {
        let urlString: String = "https://isi-open-mall.surge.sh/#/profile"
            VStack {
//                Text("Open Mall").font(.headline)
//                Text("Email").font(.subheadline)
                WebView(url: URL(string: urlString)!)
                    .cornerRadius(0)
                    .navigationBarTitleDisplayMode(.inline)
        }
    }
}

struct ProfileView_Previews: PreviewProvider {
    static var previews: some View {
        ProfileView()
    }
}
