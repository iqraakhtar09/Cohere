from django.shortcuts import render

# Create your views here.


def home(request):
    text = request.POST.get('text')
    print(text)
    # text = 'sajeel'

    if request.method == 'POST':
        import cohere
        co = cohere.Client('GxU8XjEKA2SIrK1IB1b8eJPflDRLXVNBTIlblupP')

            
        from cohere.classify import Example

        examples=[
        Example("The order came 5 days early", "positive"), 
        Example("it is good", "positive"), 
        Example("The order came 5 days early", "positive"), 
        Example("The order came 5 days early", "positive"), 
        Example("The item exceeded my expectations", "positive"), 
        Example("I ordered more for my friends", "positive"), 
        Example("I would buy this again", "positive"), 
        Example("I would recommend this to others", "positive"), 
        Example("The package was damaged", "negative"), 
        Example("The order is 5 days late", "negative"), 
        Example("The order was incorrect", "negative"), 
        Example("I want to return my item", "negative"), 
        Example("The item\'s material feels low quality", "negative"), 
        Example("The product was okay", "neutral"), 
        Example("I received five items in total", "neutral"), 
        Example("I bought it from the website", "neutral"), 
        Example("I used the product this morning", "neutral"), 
        Example("The product arrived yesterday", "neutral"),
        ]
        if text == '':
            text='sajeel'
        inputs=[
        text,
        ]

        response = co.classify(
        inputs=inputs,
        examples=examples,
        )

        res =  response.classifications[0]
        # str(res)
        # res.split(":")
        # print(res)
        # print(res[0]['Classification<prediction'])

        context={'res':res, 'text':text}
        return render(request, 'base/home.html', context)
    context={}
    return render(request, 'base/home.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)
