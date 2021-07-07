from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.shortcuts import reverse
from django.http import Http404
import json as JSON
import time
from collections import Counter
from django.http.response import HttpResponse
import heapq
import numpy as np


from py2neo import Graph
graph = Graph("http://localhost:7474", auth=("neo4j", "990910lhylhy"))


def home(request):
    if request.method == "POST":
        kword = request.POST.get('name_title')
        print(kword)
        if len(kword) == 0:
            return render(request, 'kg/home.html')
            # return HttpResponse("Please input a key word")
        else:
            if kword.count(',') == 0:
                # chord_data, numberNN, numberShow, data1, data2 = pie(kword)
                # print(chord_data)
                return render(request, 'kg/search1.html', context={"entity": kword})
                    # , "chord_data": chord_data, "numberNN": numberNN, "numberShow": numberShow, "data1": data1, "data2": data2})
            elif kword.count(',') == 1:
                return render(request, 'kg/search2.html', context={"entity": kword})
    else:
        print('else')
        return render(request, 'kg/home.html')


def pie(kword):
    c1 = 'MATCH (a)-[r]->(n) WHERE a.entityName=\'' + kword + '\' RETURN labels(a),labels(n),type(r),count(n)'
    s1 = graph.run(c1).data()
    label = []
    typeR = []
    numberNN = 0
    labelA = s1[0]['labels(a)']
    for i in range(len(s1)):
        label.append(s1[i]['labels(n)'][0])
        typeR.append(s1[i]['type(r)'])
        numberNN += s1[i]['count(n)']
    lab = list(dict(Counter(label)).keys())
    countlab = list(dict(Counter(label)).values())
    typ = list(dict(Counter(typeR)).keys())
    counttyp = list(dict(Counter(typeR)).values())
    data1 = []
    data2 = []
    for i in range(len(lab)):
        temp = dict()
        temp['y'] = countlab[i]
        temp['label'] = lab[i]
        data1.append(temp)
    for i in range(len(typ)):
        temp = dict()
        temp['y'] = counttyp[i]
        temp['label'] = typ[i]
        data2.append(temp)
    if numberNN >= 50:
        numberShow = 50
    else:
        numberShow = numberNN

    chord_data = []
    for i in range(len(lab)):
        temp_list = []
        temp_list.append(labelA[0])
        temp_list.append(lab[i])
        temp_list.append(countlab[i])
        chord_data.append(temp_list)
    return chord_data, numberNN, numberShow, data1, data2


def preheat():
    print('start preheating')
    start = time.time()
    c1 = 'MATCH (n) OPTIONAL MATCH (n)-[r]->() RETURN count(n.name) + count(r);'
    graph.run(c1)
    mid = time.time()
    print('preheating used', mid - start, 's')


def get_graph(request, entity):
    kword = entity
    if kword.count(',') == 0:
        element = get_node_edges_1(kword)
    elif kword.count(',') == 1:
        element = get_node_edges_2_new_new(kword)
    elements = {"elements": element}
    return JsonResponse(elements)


def get_node_edges_1(kword):
    if kword:
        print(kword)
        c1 = 'MATCH (a)-[r]->(n) WHERE a.entityName=\'' + kword + '\' RETURN a,n,r,labels(n),type(r),n.entityImportance'
        start = time.time()
        s1 = graph.run(c1).data()
        selected = select_node_edges(s1, 50)
        nodes = list(map(buildSelf, selected)) + list(map(buildNodes, selected))
        edges = list(map(buildEdges, selected))
        elements = {"nodes": nodes, "edges": edges}
        mid = time.time()
        print(mid - start)
    return elements


def get_node_edges_2(kword):
    kword = kword.replace(', ', ',')
    kword1 = kword.split(',')[0]
    kword2 = kword.split(',')[1]
    print(kword1,',',kword2)
    c1 = 'MATCH p=allShortestPaths((n1{entityName:\''+kword1+'\'})-[*]->(n2{entityName:\''+kword2+'\'})) return p'
    start = time.time()
    ### time start
    s1 = graph.run(c1).data()
    nodes = []
    edges = []
    for i in range(len(s1)):
        nodes = nodes + list(map(buildNodes2, s1[i]['p'].nodes))
        edges = edges + list(map(buildEdges2, s1[i]['p'].relationships))
    elements = {"nodes": nodes, "edges": edges}
    ### time end
    mid = time.time()
    print(mid - start)
    return elements


def get_node_edges_2_new(kword):
    kword = kword.replace(', ', ',')
    kword1 = kword.split(',')[0]
    kword2 = kword.split(',')[1]
    print(kword1,',',kword2)
    c1 = 'MATCH p=(n1{entityName:\'' + kword1 + '\'})-[*0..2]->(n2{entityName:\'' + kword2 + '\'}) return p'
    # c1 = 'MATCH p=allShortestPaths((n1{entityName:\''+kword1+'\'})-[*]->(n2{entityName:\''+kword2+'\'})) return p'
    start = time.time()
    ### time start
    s1 = graph.run(c1).data()
    print(len(s1))
    temp_list = []
    if len(s1) > 20:
        for i in range(len(s1)):
            count = 0
            for j in range(len(s1[i]['p'].nodes)):
                count += float(s1[i]['p'].nodes[j]['entityImportance'])
            temp_list.append(count)
        filtered = []
        max_number = heapq.nlargest(20, temp_list)
        for t in max_number:
            index = temp_list.index(t)
            filtered.append(index)
            temp_list[index] = 0
    else:
        filtered = [i for i in range(len(s1))]
    nodes = []
    edges = []
    for i in range(len(s1)):
        if i in filtered:
            print(s1[i]['p'])
            nodes = nodes + list(map(buildNodes2, s1[i]['p'].nodes))
            edges = edges + list(map(buildEdges2, s1[i]['p'].relationships))
    elements = {"nodes": nodes, "edges": edges}
    print(elements)
    ### time end
    mid = time.time()
    print(mid - start)
    return elements


def get_node_edges_2_new_new(kword):
    kword = kword.replace(', ', ',')
    kword1 = kword.split(',')[0]
    kword2 = kword.split(',')[1]
    print(kword1,',',kword2)
    c1 = 'MATCH p=allShortestPaths((n1{entityName:\'' + kword1 + '\'})-[*]->(n2{entityName:\'' + kword2 + '\'})) return p'
    ### time start
    start = time.time()
    s1 = graph.run(c1).data()
    print(len(s1))
    importance = []
    relationship_types = []
    diversity = []
    if len(s1) > 20:
        # importance
        for i in range(len(s1)):
            count = 0
            for j in range(len(s1[i]['p'].nodes)):
                count += float(s1[i]['p'].nodes[j]['entityImportance'])
            importance.append(count)
            for j in range(len(list(s1[i]['p'].relationships))):
                relationship_types.append(list(s1[i]['p'].relationships[j].types())[0])
        # diversity
        type_dict = dict(Counter(relationship_types))
        for i in range(len(type_dict)):
            type_dict[list(type_dict.keys())[i]] = 1 - (list(type_dict.values())[i] / len(s1))
        for i in range(len(s1)):
            count_diversity = 0
            for j in range(len(list(s1[i]['p'].relationships))):
                count_diversity += type_dict[list(s1[i]['p'].relationships[j].types())[0]]
            diversity.append(count_diversity)
        # integral
        filtered = []
        sum_value = list(0.6*np.array(importance) + 0.4*np.array(diversity))
        print('sum_value1:', sum_value)
        max_number = heapq.nlargest(20, sum_value)
        for t in max_number:
            index = sum_value.index(t)
            filtered.append(index)
            sum_value[index] = 0
        print('importance:', importance)
        print('diverisity:', diversity)
        print('sum_value2:', sum_value)
    else:
        filtered = [i for i in range(len(s1))]
    nodes = []
    edges = []
    for i in range(len(s1)):
        if i in filtered:
            print(s1[i]['p'])
            nodes = nodes + list(map(buildNodes2, s1[i]['p'].nodes))
            edges = edges + list(map(buildEdges2, s1[i]['p'].relationships))
    elements = {"nodes": nodes, "edges": edges}
    print(elements)
    ### time end
    mid = time.time()
    print(mid - start)
    return elements


def buildSelf(nodeRecord):
    data = {"id": nodeRecord['a'].identity, "label": list(nodeRecord['a'].labels)[0],
            "name": nodeRecord['a']['entityName'], "entityId": nodeRecord['a']['entityId'],
            "entityImportance": nodeRecord['a']['entityImportance'],
            "entityProperty": nodeRecord['a']['entityProperty']}
    return {"data": data}


def buildNodes(nodeRecord):
    data = {"id": nodeRecord['n'].identity, "label": list(nodeRecord['n'].labels)[0],
            "name": nodeRecord['n']['entityName'], "entityId": nodeRecord['n']['entityId'],
            "entityImportance": nodeRecord['n']['entityImportance'],
            "entityProperty": nodeRecord['n']['entityProperty']}
    return {"data": data}


def buildEdges(relationRecord):
    data = {"id": relationRecord['r'].identity,
            "source": relationRecord['r'].start_node.identity,
            "target": relationRecord['r'].end_node.identity,
            "relationship": list(relationRecord['r'].types())[0],
            "direction": relationRecord['r']['inverse']}
    return {"data": data}


def buildNodes2(nodeRecord):
    data = {"id": nodeRecord.identity, "label": list(nodeRecord.labels)[0],
            "name": nodeRecord['entityName'], "entityId": nodeRecord['entityId'],
            "entityImportance": nodeRecord['entityImportance'],
            "entityProperty": nodeRecord['entityProperty']}
    return {"data": data}


def buildEdges2(relationRecord):
    data = {"id": relationRecord.identity,
            "source": relationRecord.start_node.identity,
            "target": relationRecord.end_node.identity,
            "relationship": list(relationRecord.types())[0],
            "direction": relationRecord['inverse']}
    return {"data": data}


def select_node_edges(s1, k):
    # extract all data in lists
    a = []
    n = []
    r = []
    importance = []
    label = []
    for i in range(len(s1)):
        a.append(s1[i]['a'])
        n.append(s1[i]['n'])
        r.append(s1[i]['r'])
        importance.append(float(s1[i]['n.entityImportance']))
        label.append(s1[i]['labels(n)'][0])
    # select nodes and edges
    entity_temp = n
    relationship_temp = r
    coverage = [1 for i in range(len(importance))]
    selected_entity = list()
    selected_relationship = list()
    # if number of entities is bigger than limit number of entities
    if len(importance) >= k:
        count = 0
        lamb = 0.6
        while count < k:
            values = list()
            # calculate value of all entity and select the biggest one
            for i in range(len(importance)):
                v = lamb * importance[i] + (1 - lamb) * coverage[i]
                values.append(v)
            max_index = values.index(max(values))
            # add selected entity into list 'selected'
            selected_entity.append(entity_temp[max_index])
            selected_relationship.append(relationship_temp[max_index])
            # store label name as a variable
            label_name = label[max_index]
            # delete selected entity from four lists
            del entity_temp[max_index]
            del relationship_temp[max_index]
            del importance[max_index]
            del label[max_index]
            del coverage[max_index]
            # change coverage of entity with selected label to 0
            for i in range(len(coverage)):
                if label[i] == label_name:
                    coverage[i] = 0
            count += 1
    else:
        selected_entity = entity_temp
        selected_relationship = relationship_temp
    # integral as a new graph list
    selected = []
    for i in range(len(selected_entity)):
        dic = dict()
        dic['a'] = a[i]
        dic['n'] = selected_entity[i]
        dic['r'] = selected_relationship[i]
        selected.append(dic)
    return selected
