from ..models import Blog
from django.shortcuts import render
from .Tool.Tools import get_blog 
from django.shortcuts import render
from brownie import project, accounts
from django.shortcuts import render, redirect
from brownie import Contract, accounts
from brownie import web3
import brownie

acct = brownie.accounts.add("6021d22205954e378994c07b70dae0afd8e67b5eb61c8f799ebfd24f5f010708")
print(acct.address)
print(accounts[0])


acc = '0x1672b7D6a3A78871E35B83364d3b1b4aecB53924'
abi = """[
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_title",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_content",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_category",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_thumbnail",
				"type": "string"
			}
		],
		"name": "createArticle",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_title",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_content",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_category",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_thumbnail",
				"type": "string"
			}
		],
		"name": "updateArticle",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "articleCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "articles",
		"outputs": [
			{
				"internalType": "string",
				"name": "title",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "content",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "category",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "thumbnail",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			}
		],
		"name": "getArticle",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "listArticles",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "title",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "description",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "content",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "category",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "thumbnail",
						"type": "string"
					}
				],
				"internalType": "struct MyContract.Article[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]"""




def save_blog(request):
  # Replace with the actual contract address
    if request.method == 'POST':
        # Get the address and ABI of your deployed contract and ABI
        contract = Contract.from_abi('MyContract', address=acc, abi=abi)
        ids = ['#title','#description','#content','#Category','#Thumbnail']
        title = request.POST.get(ids[0])
        description = request.POST.get(ids[1])
        content = request.POST.get(ids[2])
        category = request.POST.get(ids[3])
        thumbnail = request.POST.get(ids[4])
        account = accounts[0]
        contract.createArticle(title, description, content, category, thumbnail, {'from': account})

        tx_hash = contract.createArticle(title, description, content, category, thumbnail, {'from': web3.eth.accounts[0]})

        # Wait for the transaction to be mined
        web3.eth.waitForTransactionReceipt(tx_hash)


        obj = Blog(title=title,description=description,content=content,categories=category,blog_profile_img=thumbnail)
        obj.save()
    return render(request, 'BlogBuilder/blog_edit.html')



def blog_edit(request):
    return render(request,"BlogBuilder/blog_edit.html")


def save_edit_blog(request,pk):
    ids = ['#title','#description','#content','#Category','#Thumbnail']
    title = request.POST.get(ids[0])
    description = request.POST.get(ids[1])
    content = request.POST.get(ids[2])
    Category = request.POST.get(ids[3])
    Thumbnail = request.POST.get(ids[4])

    obj = Blog.objects.get(id=pk)
    obj.content = content
    obj.title = title
    obj.description = description
    obj.categories = Category
    obj.blog_profile_img = Thumbnail
    obj.save()
    # Create a Brownie contract object using the contract address and ABI
    contract = Contract.from_abi('MyContract', acc, abi)

    # Get the current data for the article with the given ID
    article_data = contract.getArticle(pk)

    if request.method == 'POST':
        # Get the updated data from the form
        updated_title = request.POST.get('title')
        updated_description = request.POST.get('description')
        updated_content = request.POST.get('content')
        updated_category = request.POST.get('category')
        updated_thumbnail = request.POST.get('thumbnail')

        # Call the updateArticle function on the contract to update the data
        try:
            contract.updateArticle(pk, updated_title, updated_description, updated_content, updated_category, updated_thumbnail, {'from': accounts[0]})
        except Exception as e:
            return render(request, 'BlogBuilder/blog_edit.html', {'article': article_data, 'error_message': str(e)})


    return render(request,"BlogBuilder/blog_edit.html")


def list_blog(request):
    items = get_blog()
    return render(request,"BlogBuilder/Blog.html",{'blogs':items})

def view_blog(request,pk):
    page = Blog.objects.get(id=pk)
    items = get_blog()
    return render(request,"BlogBuilder/view_Blog.html",{'blog':page,'item':items})

def delete_blog(request):
    bl_id = request.GET.get("id")
    page = Blog.objects.get(id=bl_id)
    page.delete()
    contract = Contract.from_abi('MyContract', acc, abi)
    account = accounts[0]
    contract.deleteArticle(id, {'from': {'from': account}})
    return render(request,"BlogBuilder/view_Blog.html",{'blog':page})

def list_edit_blog(request):
    items = get_blog()
    return render(request,"BlogBuilder/edit_blog_list.html",{'blogs':items})

def edit_blog(request,pk):
    obj = Blog.objects.get(id=pk)
    return render(request,"BlogBuilder/blog_re_edit.html",{'obj':obj})
